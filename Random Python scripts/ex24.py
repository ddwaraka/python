def sec_for(started):
    jelly = started*1000
    jars = jelly/1000
    crates = jars//100
    return jelly, jars, crates

def show():
    #print "Results for %s", %started
    print "Beans = %d" %beans
    print "Jars = %d" %jars
    print "Crates = %d" %crates
    

start = 10000
beans, jars, crates = sec_for(start)
show()

start2 = 5000
sec_for(start2)
print jelly


