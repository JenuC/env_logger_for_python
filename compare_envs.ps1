# Path to comparison script
$comparisonScript = "compare_envs.py"

# Get all pip log files ending in '-watermark_pip.log' in the current directory
$pipLogs = Get-ChildItem -Path . -Filter *-watermark_pip.log | Select-Object -ExpandProperty FullName

# Optional: sort alphabetically
$pipLogs = $pipLogs | Sort-Object

# Print what will be compared
Write-Host "🧪 Comparing environments:"
$pipLogs | ForEach-Object { Write-Host " - $_" }

# Run the Python comparison script with all pip logs
# You can redirect output to a file if needed
python $comparisonScript @pipLogs > "env_comparison_output.txt"

Write-Host "`n✅ Comparison complete. Output saved to env_comparison_output.txt"
