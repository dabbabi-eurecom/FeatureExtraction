# python script for determining the polarity and POS caracteristics
# of an input tweet using SentiWordNet3.0 dictionnary

# load input file in a dictionnary
def loadSentiSimple(filename):
    output={}
    print "Opening SentiWordnet file..."
    fi=open(filename,"r")
    line=fi.readline() # skip the first header line
    line=fi.readline()
    print "Loading..."

    while line:
        l=line.split('\t')
        tag=l[0]
        word=l[1]
        pos=abs(float(l[3]))
        neg=abs(float(l[4]))
        neu=abs(float(l[5]))

        output[word]=[tag,pos,neg,neu]
        line=fi.readline()
    fi.close()
    return output

def loadSentiFull(filename):
    output={}
    print "Opening SentiWordnet file..."
    fi=open(filename,"r")
    line=fi.readline() # skip the first header line
    line=fi.readline()
    print "Loading..."

    while line:
#        print line
        l=line.split('\t')
        try:
            tag=l[0]
            word=l[4].split()[0][:-2]
            pos=abs(float(l[2]))
            neg=abs(float(l[3]))
            neu=float(1-pos-neg)
        except:
            print line
            line=fi.readline()
            continue

        output[word]=[tag,pos,neg,neu]
        line=fi.readline()
    fi.close()
    return output

def polarity(tweet,sentDict): # polarity saggregate of a tweet from sentiWordnet dict
    pos=0.0
    neg=0.0
    neu=0.0
    for w in tweet:
        pos=pos+sentDict[w][1]
        neg=neg+sentDict[w][2]
        neu=neu+sentDict[w][3]
    return [pos,neg,neu]

INPUT_FILENAME="../resources/sentiWordnetBig.csv"
dict=loadSentiFull(INPUT_FILENAME)
print len(dict.keys())
# still some work to finish and to add some synonyms
# POS tags in a function



