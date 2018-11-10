<?php
$inactive=10;
session_start();
if(isset($_SESSION["time"]) && ((time()-$_SESSION["time"])>$inactive))
{
		echo "HI";
	session_destroy();
	header("Location: loginForm.php");
}
$_SESSION["time"]=time();
?>
<html>
<body>
<h1>Welcome!</h1>
</body>
</html>