<head>
</head>
<body>
<form name="form" onclick="hello()" action="main.php" method="get" onclic>
  <input type="text" name="Myname" id="Myname" value="SonDepTrai">
  <input type="submit" value="Submit">
</form>

<p> This is output </p>
<p style="font-size:20px;">
<?php
    
    // function hello(){
        $clgt = $_GET['Myname'];
        $command = escapeshellcmd('python process.py ' . $clgt);
        $output = shell_exec($command);
        echo $output;
    // }
    
?>
</p>
