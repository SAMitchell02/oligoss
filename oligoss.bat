@echo off

set i=""
set r=""
set o=""

:initial
if "%1"=="" goto done
echo %1
set aux=%1
if "%aux:~0,1%"=="-" (
   set nome=%aux:~1,250%
) else (
   if "%nome%"=="i" set i=%aux%
   if "%nome%"=="r" set r=%aux%
   if "%nome%"=="o" set o=%aux%
   set nome=
)
shift
goto initial
:done

set INPUT_PARAMS=%i%
set OUTPUT_DIR=%o%
set RIPPER=%r%

IF "%INPUT_PARAMS%"=="" (
  echo "No input parameters (-i) given"
  exit /b 1
)
IF "%OUTPUT_DIR%"=="" (
  echo "No output directory (-o) given"
  exit /b 1
)
IF "%RIPPER%"=="" (
  echo "No input data directory (-r) given"
  exit /b 1
)

docker run -it --mount type=bind,source="%INPUT_PARAMS%",target=/input_parameters.json -v "%RIPPER%":/data -v "%OUTPUT_DIR%":/output oligoss:latest