
import sys, os, time
import numpy as np
from scipy.stats import pearsonr, hypergeom
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

PRIMES = [2,3,5,7,11,13,17,19,23,29,31,37]
N_SHUFFLE = 500
N_GUE = 300
N_SIZES = [500,1000,2000,5000,10000]
MAX_LAG = 50
TOP_K = 12
SEP = "=" * 60

def load_zeros(path=None):
    for p in [path,"zeros3.txt","zeros2.txt","zeros4.txt"]:
        if p and os.path.exists(p):
            g = np.loadtxt(p)
            print(f"  Loaded {len(g):,} zeros from {p}")
            return g, p
    print("  [INFO] No zero file — using synthetic GUE data.")
    print("  Download: http://www-users.cse.umn.edu/~odlyzko/zeta_tables/")
    rng = np.random.default_rng(42)
    u = rng.uniform(0,1,10000)
    sp = np.sqrt(-4/np.pi*np.log(1-u+1e-10))
    return 1e12+np.cumsum(sp), "synthetic_GUE"

def cov_lags(gamma, lags):
    d = np.diff(gamma); d -= d.mean()
    return np.array([np.mean(d[:-h]*d[h:]) if len(d)>h+10 else 0.0 for h in lags])

def bk(primes):
    lp = np.log(np.array(primes,float))
    return lp**2/np.array(primes,float)

def wigner(n, rng):
    u = rng.uniform(0,1,n)
    return np.sqrt(-4/np.pi*np.log(1-u+1e-10))

def run_all():
    zeros_file = sys.argv[1] if len(sys.argv)>1 else None
    rng = np.random.default_rng(42)
    lines = []
    def log(msg=""):
        print(msg); lines.append(msg+"\n")

    print(SEP)
    print("BK Control Test Suite — run_all.py")
    print("Experimental investigation: prime-related structure in zeta zero statistics")
    print(SEP)

    gamma, source = load_zeros(zeros_file)
    Bp = bk(PRIMES)
    log(f"Source: {source} | N={len(gamma):,}")

    t0 = time.time()
    Ap_real = cov_lags(gamma, PRIMES)
    r_real, pv_real = pearsonr(Ap_real, Bp)

    # T1: Shuffled
    print("\n[1/5] Shuffled zeros permutation test...")
    log(SEP); log("TEST 1: Shuffled Zeros")
    log(f"  Real: r={r_real:.4f}  p={pv_real:.3e}")
    r_null = []
    for _ in range(N_SHUFFLE):
        d = np.diff(gamma); rng.shuffle(d)
        g = gamma[0]+np.concatenate([[0],np.cumsum(np.abs(d))])
        r_s,_ = pearsonr(cov_lags(g,PRIMES),Bp)
        r_null.append(r_s)
    r_null = np.array(r_null)
    p1 = np.mean(r_null>=r_real)
    log(f"  Null: mean={r_null.mean():.4f} std={r_null.std():.4f}")
    log(f"  Empirical p={p1:.4f} | {'SIGNAL>NULL' if p1<0.05 else 'NOT SIGNIFICANT'}")
    fig,ax=plt.subplots(figsize=(8,4))
    ax.hist(r_null,bins=40,color='steelblue',alpha=0.75,label='Null (shuffled)')
    ax.axvline(r_real,color='red',lw=2,label=f'Real r={r_real:.4f}')
    ax.set_xlabel('Pearson r'); ax.set_ylabel('Count')
    ax.set_title('Test 1: Shuffled Zeros'); ax.legend()
    plt.tight_layout(); plt.savefig('results_01_shuffled.png',dpi=150); plt.close()

    # T2: GUE
    print("[2/5] GUE surrogate test...")
    log(SEP); log("TEST 2: GUE Surrogate")
    r_gue = []
    for _ in range(N_GUE):
        g = gamma[0]+np.cumsum(wigner(len(gamma),rng))
        r_g,_ = pearsonr(cov_lags(g,PRIMES),Bp)
        r_gue.append(r_g)
    r_gue=np.array(r_gue)
    p2=np.mean(r_gue>=r_real)
    log(f"  GUE: mean={r_gue.mean():.4f} 95th={np.percentile(r_gue,95):.4f}")
    log(f"  Empirical p={p2:.4f} | {'EXCEEDS GUE' if p2<0.05 else 'WITHIN GUE'}")
    fig,ax=plt.subplots(figsize=(8,4))
    ax.hist(r_gue,bins=35,color='steelblue',alpha=0.75,label='GUE surrogates')
    ax.axvline(r_real,color='red',lw=2,ls='--',label=f'Real r={r_real:.4f}')
    ax.set_xlabel('Pearson r'); ax.legend()
    ax.set_title('Test 2: GUE Surrogate vs Real')
    plt.tight_layout(); plt.savefig('results_02_gue.png',dpi=150); plt.close()

    # T3: Scaling
    print("[3/5] Scaling law test...")
    log(SEP); log("TEST 3: Scaling Law r vs N")
    sc_r={}
    for N in N_SIZES:
        g=gamma[:min(N,len(gamma))]
        r,_=pearsonr(cov_lags(g,PRIMES),Bp)
        sc_r[N]=r; log(f"  N={N:>6,}: r={r:.4f}")
    vals=list(sc_r.values())
    trend="STABLE" if max(vals)-min(vals)<0.3 else "VARIABLE"
    log(f"  Range: {min(vals):.4f}-{max(vals):.4f} ({trend})")
    fig,ax=plt.subplots(figsize=(7,4))
    ax.plot(N_SIZES,vals,'o-',color='steelblue',lw=2)
    ax.set_xscale('log'); ax.set_xlabel('N'); ax.set_ylabel('Pearson r')
    ax.set_title('Test 3: Scaling Law'); ax.grid(True,alpha=0.3)
    plt.tight_layout(); plt.savefig('results_03_scaling.png',dpi=150); plt.close()

    # T4: Window
    print("[4/5] Window stability test...")
    log(SEP); log("TEST 4: Window Stability")
    wins={'Rectangular':None,'Hann':np.hanning,'Blackman':np.blackman,'Hamming':np.hamming}
    wr={}
    for name,wfn in wins.items():
        d=np.diff(gamma); d-=d.mean()
        if wfn: d*=wfn(len(d))
        Ap=[np.mean(d[:-p]*d[p:]) if len(d)>p+10 else 0.0 for p in PRIMES]
        r,_=pearsonr(np.array(Ap),Bp)
        wr[name]=r; log(f"  {name:15} r={r:.4f}")
    rng_w=max(wr.values())-min(wr.values())
    wv="STABLE" if rng_w<0.3 else "SENSITIVE"
    log(f"  Range={rng_w:.4f} ({wv})")
    fig,ax=plt.subplots(figsize=(8,4))
    ax.barh(list(wr.keys()),list(wr.values()),color='steelblue',alpha=0.8)
    ax.set_xlabel('Pearson r'); ax.set_title('Test 4: Window Stability')
    ax.axvline(0,color='gray',lw=0.8)
    plt.tight_layout(); plt.savefig('results_04_window.png',dpi=150); plt.close()

    # T5: Blind
    print("[5/5] Blind peak detection test...")
    log(SEP); log("TEST 5: Blind Peak Detection")
    lags=np.arange(1,MAX_LAG+1)
    d=np.diff(gamma); d-=d.mean()
    covs=np.array([np.mean(d[:-h]*d[h:]) if len(d)>h+10 else 0.0 for h in lags])
    pm=covs>0; pl=lags[pm]; pv2=covs[pm]
    ti=np.argsort(pv2)[-TOP_K:]
    tl=set(pl[ti]); ps=set(PRIMES)
    ov=len(ps&tl)
    p5=hypergeom.sf(ov-1,MAX_LAG,len(PRIMES),TOP_K)
    log(f"  Top-{TOP_K}: {sorted(tl)}")
    log(f"  Overlap: {ov}/{TOP_K} | Expected: {TOP_K*len(PRIMES)/MAX_LAG:.2f}")
    log(f"  Hypergeometric p={p5:.4f} | {'PRIME-SPECIFIC' if p5<0.05 else 'NOT SIGNIFICANT'}")
    fig,ax=plt.subplots(figsize=(10,4))
    cols=['tomato' if l in ps else 'limegreen' if l in tl else 'steelblue' for l in lags]
    ax.bar(lags,covs,color=cols,alpha=0.8,width=0.6)
    ax.axhline(0,color='gray',lw=0.8,ls='--')
    ax.set_xlabel('Lag h'); ax.set_ylabel('C(h)')
    ax.set_title(f'Test 5: Blind Detection (overlap={ov}/{TOP_K}, p={p5:.3f})\nRed=prime | Green=detected')
    plt.tight_layout(); plt.savefig('results_05_blind.png',dpi=150); plt.close()

    elapsed=time.time()-t0
    log(SEP); log("SUMMARY")
    log(SEP)
    log(f"Source: {source} | N={len(gamma):,}")
    log(f"Real r={r_real:.4f}  p={pv_real:.3e}")
    log(f"T1 shuffle:  p={p1:.4f}")
    log(f"T2 GUE:      p={p2:.4f}")
    log(f"T3 scaling:  {trend}")
    log(f"T4 window:   {wv}")
    log(f"T5 blind:    overlap={ov}/{TOP_K} p={p5:.4f}")
    log()
    log("CAVEATS:")
    log("  Computational observations only — not a confirmed result")
    log("  p-values assume independence (may be violated)")
    log("  Normalization choice affects results")
    log("  Independent replication required")
    log(f"\nRuntime: {elapsed:.1f}s")
    with open("summary_report.txt","w") as f:
        f.writelines(lines)
    print(SEP)
    print("Done. See summary_report.txt and results_*.png")
    print(SEP)

if __name__=="__main__":
    run_all()
