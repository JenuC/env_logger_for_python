

$BOCK103envs = @( 
    ".venv",
    "napari_env",
    ".napari_sam_v2",
    ".napari_sam_MIC-DKFZ"
)
$envs = $BOCK103envs

foreach ($env_name in $envs) {

    Write-Host "`n🔧 Checking environment: $env_name"
    # Set environment name :: Activate virtual environment
    & ".\$env_name\Scripts\Activate.ps1"
    & ".\enable_cuda_11.ps1"

    python --version
    python check_versions.py --save "$env_name-version-check.log"
    uv pip list > "$env_name-watermark_pip.log"
    # Optional: deactivate env (if needed in your workflow)
    deactivate
}


