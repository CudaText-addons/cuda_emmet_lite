echo Extract: 
nodejs runner.js extract "<html><body>ul*2>li*3"
echo " "
echo Expand: 
nodejs runner.js expand "ul*2>li*3" "html" "html"
