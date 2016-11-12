<!DOCTYPE html>

<html>
  <head>
    <title>Welcome</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>

  </head>

<body>
This is your list
<table border="1">
%for task in tasks:
<tr>
	<td>{{task}}</td>
	<td><a href="/delete"><img src="/static/trash.png" style="width:16px;height:16px;border:0;"/></a></td>
		</tr>
%end
</table>
</body>
				
</body>
