Invoke-WebRequest https://bitbucket.org/cegui/cegui/get/v0-8.zip -OutFile cegui_v0-8.zip
7z x cegui_v0-8.zip -ocegui
#Thanks to TheMadTechnician (http://stackoverflow.com/questions/28843448/powershell-getting-foldername-like-and-get-the-first-subdirectory)
Function GCI-ToDepth{
Param(
    $Path = $PWD.Path,
    $Filter = "*",
    $Depth = 255
    )

    $Paths = 1..$Depth|ForEach{"{0}{1}" -f $Path.trimend('\'), ("\*" * $_)}
    Get-ChildItem -Path $Paths -Filter $Filter
}
$tmp_dir = GCI-ToDepth -Path "cegui" -Depth 1
move $tmp_dir\* cegui
rm $tmp_dir
