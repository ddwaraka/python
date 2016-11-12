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
		</body>
	</html>