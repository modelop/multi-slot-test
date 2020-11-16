#modelop.slot.0:in-use
#modelop.slot.1:in-use
#modelop.slot.2:in-use

#modelop.init
def begin():
    """
    initialize global var x @ zero
    """
    global x
    x = 0
    pass

#modelop.score
def action(datum, slot_no):
    
    # An input to the second slot should trigger
    # the update function
    if slot_no == 2:
        # Increment the global var x by input datum
        update(datum)
        print(x, flush=True)
        return
    
    # If the input slot is 0, increment by original x
    datum += x
    
    yield datum

#modelop.metrics
def metrics(data):
    yield {"f1": 0.3, "AUC": 0.7}

def update(datum):
    
    #increment global var x by datum
    global x
    x += datum

