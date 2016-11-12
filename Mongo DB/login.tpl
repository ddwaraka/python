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
            Username
          </td>
          <td>
            <input type="text" name="username" value="{{username}}">
          </td>
          <td class="error">
          </td>
        </tr>

        <tr>
          <td class="label">
            Password
          </td>
          <td>
            <input type="password" name="password" value="">
          </td>
          <td class="error">
	    {{login_error}}
            
          </td>
        </tr>

      </table>

      <input type="submit" value="Login">
    </form>
  </body>

</html>