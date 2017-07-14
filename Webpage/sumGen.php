<?php
  	


  	$q = $_POST["q"];
//  	echo $q;
 // 	exec("python sumgen.py $q > out");
  //	$echo "ere";
  	//$out = file_get_contents(out);
  	// echo system("ls");
  	//echo($q)
  	system('python sumgen.py '.$q.'', $output);
  	echo implode("\n", $output);
  	//echo $out;
      
  //  echo $out;
?>