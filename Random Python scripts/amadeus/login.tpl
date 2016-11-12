<!DOCTYPE html>

<html>
  <head>
    <title>Login</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>

  </head>

  <body>
  <p><a href="/">Home</a>&nbsp&nbsp&nbsp<a href="/about">About</a><p>
    <h2>Login</h2>
    <form method="post">
      <table>
        <tr>
          <td class="label">
            Origin
          </td>
          <td>
            <input type="text" name="origin" value="{{origin}}">
          </td>
          <td class="error">
          </td>
        </tr>

        <tr>
          <td class="label">
            Destination
          </td>
          <td>
            <input type="text" name="destination" value="{{destination}}"">
          </td>
          <td class="error">
	    {{place_error}}
            
          </td>
        </tr>
        
        tr>
          <td class="label">
            Date
          </td>
          <td>
            <input type="text" name="date" value="{{date}}"">
          </td>
          <td class="error">
	    {{date_error}}
            
          </td>
        </tr>

      </table>

      <input type="submit" value="Login">
    </form>
  </body>

</html>