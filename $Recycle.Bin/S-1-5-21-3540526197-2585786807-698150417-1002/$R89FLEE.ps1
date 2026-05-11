Add-Type -AssemblyName UIAutomationClient
Add-Type -AssemblyName UIAutomationTypes

$printerName = "EPSON Stylus Photo 1400 Series"
$repeatCount = 3

function Do-HeadCleaning {
    param($round)
    Write-Host "[$round/$repeatCount] Starting..." -ForegroundColor Yellow

    Start-Process "rundll32.exe" -ArgumentList "printui.dll,PrintUIEntry /p /n `"$printerName`""
    Start-Sleep -Seconds 3

    $desktop = [System.Windows.Automation.AutomationElement]::RootElement

    $condition = New-Object System.Windows.Automation.PropertyCondition(
        [System.Windows.Automation.AutomationElement]::NameProperty,
        "EPSON Stylus Photo 1400 Series Printing Preferences"
    )

    $window = $null
    for ($t = 0; $t -lt 10; $t++) {
        $window = $desktop.FindFirst([System.Windows.Automation.TreeScope]::Children, $condition)
        if ($window) { break }
        Start-Sleep -Seconds 1
    }

    if (-not $window) { Write-Host "Window not found!" -ForegroundColor Red; return }
    Write-Host "Window found!" -ForegroundColor Green

    # Maintenance tab
    $tabCond = New-Object System.Windows.Automation.PropertyCondition(
        [System.Windows.Automation.AutomationElement]::NameProperty, "Maintenance"
    )
    $tab = $window.FindFirst([System.Windows.Automation.TreeScope]::Descendants, $tabCond)
    if ($tab) {
        $tab.GetCurrentPattern([System.Windows.Automation.InvokePattern]::Pattern).Invoke()
        Write-Host "Maintenance tab clicked!" -ForegroundColor Green
        Start-Sleep -Seconds 1
    }

    # Head Cleaning button
    $cleanCond = New-Object System.Windows.Automation.PropertyCondition(
        [System.Windows.Automation.AutomationElement]::NameProperty, "Head Cleaning"
    )
    $cleanBtn = $window.FindFirst([System.Windows.Automation.TreeScope]::Descendants, $cleanCond)
    if ($cleanBtn) {
        $cleanBtn.GetCurrentPattern([System.Windows.Automation.InvokePattern]::Pattern).Invoke()
        Write-Host "Head Cleaning clicked!" -ForegroundColor Green
        Start-Sleep -Seconds 2
    }

    # Start button
    $startCond = New-Object System.Windows.Automation.PropertyCondition(
        [System.Windows.Automation.AutomationElement]::NameProperty, "Start"
    )
    $startBtn = $desktop.FindFirst([System.Windows.Automation.TreeScope]::Descendants, $startCond)
    if ($startBtn) {
        $startBtn.GetCurrentPattern([System.Windows.Automation.InvokePattern]::Pattern).Invoke()
        Write-Host "Start clicked! Waiting 120 sec..." -ForegroundColor Yellow
    }

    for ($s = 120; $s -gt 0; $s--) {
        Write-Host "`rWaiting: $s sec...   " -NoNewline
        Start-Sleep -Seconds 1
    }

    # Finish button
    $finishCond = New-Object System.Windows.Automation.PropertyCondition(
        [System.Windows.Automation.AutomationElement]::NameProperty, "Finish"
    )
    $finishBtn = $desktop.FindFirst([System.Windows.Automation.TreeScope]::Descendants, $finishCond)
    if ($finishBtn) {
        $finishBtn.GetCurrentPattern([System.Windows.Automation.InvokePattern]::Pattern).Invoke()
        Write-Host "`rFinish clicked!" -ForegroundColor Green
        Start-Sleep -Seconds 2
    }

    # Cancel / Close
    $cancelCond = New-Object System.Windows.Automation.PropertyCondition(
        [System.Windows.Automation.AutomationElement]::NameProperty, "Cancel"
    )
    $cancelBtn = $window.FindFirst([System.Windows.Automation.TreeScope]::Descendants, $cancelCond)
    if ($cancelBtn) {
        $cancelBtn.GetCurrentPattern([System.Windows.Automation.InvokePattern]::Pattern).Invoke()
    }

    Start-Sleep -Seconds 2
    Write-Host "[$round/$repeatCount] Done!" -ForegroundColor Green
}

Write-Host "EPSON Auto Head Cleaning - Total: $repeatCount rounds" -ForegroundColor Cyan
Write-Host "--------------------------------------" -ForegroundColor DarkGray

for ($i = 1; $i -le $repeatCount; $i++) {
    Do-HeadCleaning -round $i
}

Write-Host "All $repeatCount cleanings done!" -ForegroundColor Green
