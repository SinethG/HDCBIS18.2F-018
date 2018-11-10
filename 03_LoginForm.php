<?php
session_start();
if(isset($_POST["user"]) && isset($_POST["pass"]))
{
	if($_POST["user"]=="admin" && $_POST["pass"]=="123")
	{	
		$_SESSION["time"]=time();
		header("Location: NewPage.php");
	}
	
}
?>
<html>
<body>
<form name="Login" method="POST" action="#">
Username <input type="text" name="user"/><br/>
Password <input type="password" name="pass"/><br/>
<input type="submit" value="Login"/>
</form>
</body>