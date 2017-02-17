#based on https://www.appveyor.com/docs/api/samples/download-artifacts-ps/

$apiUrl = 'https://ci.appveyor.com/api'
$accountName = 'cegui-ci'
$projectSlug = 'cegui'
$branch = "v0-8"

# get project with last build details
$project = Invoke-RestMethod -Method Get -Uri "$apiUrl/projects/$accountName/$projectSlug/branch/$branch"

# Get the MSVC2015 job id
ForEach ($job in $project.build.jobs) {if ($job.name.Contains("TOOLCHAIN=msvc2015")) {$jobId = $job.jobid; break}}

# get job artifacts (just to see what we've got)
$artifacts = Invoke-RestMethod -Method Get -Uri "$apiUrl/buildjobs/$jobId/artifacts"

# here we just take the first artifact, but you could specify its file name
$artifactFileName = $artifacts[0].fileName
$localartifactFileName = [System.IO.Path]::GetFileName("$artifactFileName")

# artifact will be downloaded as
$localArtifactPath = "$env:downloadLocation\$localartifactFileName" 

# download artifact
# -OutFile - is local file name where artifact will be downloaded into
# the Headers in this call should only contain the bearer token, and no Content-type, otherwise it will fail!
Invoke-RestMethod -Method Get -Uri "$apiUrl/buildjobs/$jobId/artifacts/$artifactFileName" `
-OutFile $localArtifactPath

$folder_name = [System.IO.Path]::GetFileNameWithoutExtension("$artifactFileName")
$extract_dir = "$env:downloadLocation"
7z x $localArtifactPath -o"$extract_dir"
$env:CEGUI_DIR = "$env:downloadLocation/$folder_name"
$env:CMAKE_PREFIX_PATH ="$env:CMAKE_PREFIX_PATH;$env:CEGUI_DIR"