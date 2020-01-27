rm zip_file.zip

chmod -R 755 ./*

zip -r zip_file ./*

direnv allow
