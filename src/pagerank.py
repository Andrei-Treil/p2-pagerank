import sys
import gzip
from collections import defaultdict, Counter
import math

'''
linksFileGZ - gzipped file of links that you are analyzing.
lamb - value to use for λ (the balance between “teleportation” and following a link)
tau - value for τ (the threshold for deciding convergence)
inLinksFile - print out the list of pages with their number of in-links (see "settings and generated output" for format)
pagerankFile - print out the list of pages with their calculated pagerank value (see "settings and generated output" for format)
k - number of top pages that you print in those two files
'''
def main(linksFileGZ,lam,tau,inLinksFile,pagerankFile,k):
    #dictionary to count in links
    in_links = defaultdict(int)
    #dictionary to store pages as keys and their outlinks in a list
    pages = defaultdict(list)

    with gzip.open(linksFileGZ,'rt',encoding='utf8') as f:
        for line in f:
            edge = line.split()
            in_links[edge[0]]
            in_links[edge[1]] += 1
            pages[edge[0]].append(edge[1])
            pages[edge[1]]

    sorted_inlinks = dict(sorted(in_links.items(), key=lambda item: item[1], reverse=True))
    sites = pages.keys()
    num_pages = len(sites)

    #current page rank estimate mapping pages to their ranks
    curr_pr = dict.fromkeys(sites,1/num_pages)
    new_pr = dict.fromkeys(sites,lam/num_pages)
    '''
    While page rank hasnt converged (defined by tau), set all entries in R = λ/|P|
    For each page, check out links and update their page rank accordingly:  Rq += (1 - λ)Ip/|Q|
    If no outlinks, do random jump stuff
    '''
    not_converged = True
    while(not_converged):
        #resulting page rank estimate
        res_pr = new_pr.copy()

        #track pr of all pages with no outlinks
        no_out_sum = 0

        #loop thru all pages
        for page,links in pages.items():
            curr_page_pr = curr_pr[page]
            if len(links) == 0:
                #do random jump
                #res_pr = {p: r+((1-lam)*curr_page_pr)/num_pages for p,r in res_pr.items()}
                no_out_sum += curr_page_pr

            else:
                for out_page in links:
                    #update pagerank
                    res_pr[out_page] += ((1-lam)*curr_page_pr)/len(links)
        
        #add the pr changes for no outlink pages
        for key in res_pr:
            res_pr[key] += ((1-lam)*no_out_sum)/num_pages

        #check convergence
        if math.dist(res_pr.values(),curr_pr.values()) <= tau:
            not_converged = False
            sorted_pr = dict(sorted(res_pr.items(), key=lambda item: item[1], reverse=True))
            break

        curr_pr.update(res_pr)

    '''
    Write top 100 pageranks to pagerank.txt
    The list should be sorted in descending value of PageRank with each line having the format:
    PageName<tab>Rank<tab>PageRank score
    '''
    with open(pagerankFile,'w') as f:
        i = 1
        for page,rank in sorted_pr.items():
            f.write(page + "\t" + str(i) + "\t" + str(rank) + "\n")
            if i == k:
                break
            else:
                i += 1

    '''
    Write top 100 pages having the most inlinks to inlinks.txt
    The list should be sorted in descending frequency of inlink count with each line having the format:
    PageName<tab>Rank<tab>inlinkeCount
    '''
    with open(inLinksFile,'w') as f:
        i = 1
        for page,count in sorted_inlinks.items():
            f.write(page + "\t" + str(i) + "\t" + str(count) + "\n")
            if i == k:
                break
            else:
                i += 1

if __name__ == '__main__':
    #code from P2 instructions
    argv_len = len(sys.argv)
    inputFile = sys.argv[1] if argv_len >= 2 else "links-ireland.srt.gz"
    lambda_val = float(sys.argv[2]) if argv_len >=3 else 0.2
    tau = float(sys.argv[3]) if argv_len >=4 else 0.005
    inLinksFile = sys.argv[4] if argv_len >= 5 else "inlinks.txt"
    pagerankFile = sys.argv[5] if argv_len >= 6 else "pagerank.txt"
    k = int(sys.argv[6]) if argv_len >= 7 else 100
    main(inputFile,lambda_val,tau,inLinksFile,pagerankFile,k)