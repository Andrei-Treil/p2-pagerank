import sys
import gzip
from collections import defaultdict

'''
linksFileGZ - gzipped file of links that you are analyzing.
lamb - value to use for λ (the balance between “teleportation” and following a link)
tau - value for τ (the threshold for deciding convergence)
inLinksFile - print out the list of pages with their number of in-links (see "settings and generated output" for format)
pagerankFile - print out the list of pages with their calculated pagerank value (see "settings and generated output" for format)
k - number of top pages that you print in those two files
'''
def main(linksFileGZ,lam,tau,inLinksFile,pagerankFile,k):
    
    #dictionary to store pages as keys and their outlinks in a list
    pages = defaultdict(list)
    with gzip.open(linksFileGZ,'rt') as f:
        for edge in f.readline().split():
            pages[edge[0]].append(edge[1])

    num_pages = len(pages.keys())
    #current page rank estimate mapping pages to their ranks
    curr_pr = defaultdict(lambda: 1/num_pages)
    #resulting page rank estimate
    res_pr = defaultdict(lambda: 1/num_pages)

    '''
    While page rank hasnt converged (defined by tau), set all entries in R = λ/|P|
    For each page, check out links and update their page rank accordingly:  Rq += (1 - λ)Ip/|Q|
    If no outlinks, do random jump stuff
    '''
    not_converged = True
    while(not_converged):
        #loop thru all pages
        for page,links in pages:
            if len(links) == 0:
                #do random jump
                i = 1
            else:
                for out_page in links:
                    res_pr[out_page] += ((1-lam)*curr_pr[page])/len(out_page)

        #check convergence

        #update pagerank
        curr_pr.update(res_pr)


        return res_pr



    return None



if __name__ == '__main__':
    #code from P2 instructions
    argv_len = len(sys.argv)
    #change back to links.srt.gz
    inputFile = sys.argv[1] if argv_len >= 2 else "small.srt.gz"
    lambda_val = float(sys.argv[2]) if argv_len >=3 else 0.2
    tau = float(sys.argv[3]) if argv_len >=4 else 0.005
    inLinksFile = sys.argv[4] if argv_len >= 5 else "inlinks.txt"
    pagerankFile = sys.argv[5] if argv_len >= 6 else "pagerank.txt"
    k = int(sys.argv[6]) if argv_len >= 7 else 100
    main(inputFile,lambda_val,tau,inLinksFile,pagerankFile,k)