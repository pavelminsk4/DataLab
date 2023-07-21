<?php 
if($_SERVER['REQUEST_METHOD'] === 'POST') {
	/* add email here and bottom */
	$to = "abdelaziz4work@gmail.com";
	$subject = "Form Submission Enquirey";

	
	$name = $_POST['name'];
	$email = $_POST['email'];
	$number = $_POST['number'];
	$company = $_POST['company'];
	$job = $_POST['job'];
	$services = $_POST['services'];
	
	$messagebody = "
		<table border=0 style='width:600px;'>
		<tr><td style='width:100%'>Full Name: $name</td></tr>
		<tr><td style='width:100%'>Work Email: $email</td></tr>
		<tr><td style='width:100%'>Phone Number: $number</td></tr>
		<tr><td style='width:100%'>Company Name: $company</td></tr>
		<tr><td style='width:100%'>Job Title: $job</td></tr>
		<tr><td style='width:100%'>Required Services: $services</td></tr>
		</table>";
		
    $headers = "MIME-Version: 1.0" . "\r\n";
    $headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";
    $headers .= 'From:'.$name. '<exampel@gmail.com>' . "\r\n";
	$headers .=  "Reply-To: $email" . "\r\n" .
				'X-Mailer: PHP/' . phpversion();
				
	if(mail($to,$subject,$messagebody,$headers)){
		echo "Mail sent successfully";
	}else{
		echo "Mail not sent error";
	}
	
	
}	
?>
