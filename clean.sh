find . -name \*.pyc -delete
find . -name \*~ -delete
find . -type d -name '.ropeproject' -exec rm -rf {} \;
