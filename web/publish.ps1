npm run build
rm -R -Fo ../public
robocopy ./dist/ ../public /E /IS /IT