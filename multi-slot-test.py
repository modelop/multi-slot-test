#modelop.slot.0:in-use
#modelop.slot.1:in-use
#modelop.slot.2:in-use

baseline=None
sample=None
numerical_columns=None

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
def metrics(data, slot_no):
    global baseline, sample, numerical_columns
    if slot_no==0:
        baseline=data.copy()
        numerical_columns = baseline.select_dtypes(['int64', 'float64']).columns
    if slot_no==2:
        sample=data.copy()
    
    print(baseline, flush=True)
    print(sample, flush=True)
    print(numerical_columns, flush=True)
    if sample is not None and baseline is not None:
        yield {"foo": "bar"}
    else: return



def update(datum):
    
    #increment global var x by datum
    global x
    x += datum

