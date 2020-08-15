<html>
    <head>
        <title>run my python files</title>
    </head>


    <body>
        <link rel="stylesheet" href="box.css">
        <div id="header"> </div>
        <div id="app">
            <h1> Covid Simplified </h1>
            <div id="selectors">
                <?PHP
                    echo shell_exec("python3 interface.py");
                ?>
            </div>
            
        </div>
    </body>

    
</html>
