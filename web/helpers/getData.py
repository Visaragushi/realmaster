def getData(data, dataName, model):
    # Query all data
    query = model.objects.all()
    data[dataName] = query
    print(query)


def get_deserts(model):

    query = model.objects.filter(tipo=1)
    return query


def get_deserts2(model):

    query = model.objects.filter(tipo=2)
    return query






def get_deserts3(model):

    query = model.objects.filter(tipo=3)
    return query


def get_deserts4(model):

    query = model.objects.filter(tipo=4)
    return query

