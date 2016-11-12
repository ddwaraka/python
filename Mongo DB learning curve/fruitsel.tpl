<!DOCTYPE html>
	<html>
		<head>
			<title>Hello World!</title>
		</head>
		<body>
				Welcome to my web page<p>
				Welcome {{username}}
				<ul>
				
				%for thing in things:
				<li>{{thing}}</li>
				%end
				
				</ul>
		   
		   <form action="/favourite_fruit" method="POST">
		       What is your favourite fruit?
			   <input type="text" name="fruit" size="40" value=""><br>
			   <input type="submit" value="Submit">
		   </form>
		</body>
	</html>