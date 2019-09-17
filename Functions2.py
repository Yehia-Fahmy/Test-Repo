# Modify this function to return a list of strings as defined above
def list_benefits():
    our_list = ["Benifit#1", "Benifit#2", "Benifit#3", "Benifit#4"]
    return our_list


# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return benefit + " is the benefit of functions"


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))


name_the_benefits_of_functions()
