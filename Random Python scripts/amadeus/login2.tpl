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
            <input type="text" origin="origin" value="{{origin}}">
          </td>
          <td class="error">
          </td>
        </tr>

        <tr>
          <td class="label">
            Destination
          </td>
          <td>
            <input type="text" destination="destination" value="{{destination}}">
          </td>
          <td class="error">
	  
            
          </td>
        </tr>
        
        <tr>
          <td class="label">
           departure_date
          </td>
          <td>
            <input type="text" departure_date="departure_date" value="{{departure_date}}">
          </td>
          <td class="error">
	    
            
          </td>
        </tr>
        
         <tr>
          <td class="label">
           max_price
          </td>
          <td>
            <input type="text" max_price="max_price" value="{{max_price}}">
          </td>
          <td class="error">
	    
            
          </td>
        </tr>
        


      </table>

      <input type="submit" value="Submit">
    </form>
  </body>

</html>