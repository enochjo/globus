In the case where there are just too many files within one directory, Globus GUI will often just timeout and not display the contents of a folder. In this case, you may have to use Globus CLI to use terminal to transfer files. 

The following was done on NERSC Perlmutter (Dec 5 2024)
1. Load the appropriate modules
module load globus-tools

2. Figure out the source and destination IDs. You can do this by clicking "Get Link" within Globus File Transfer and copying the number/letter/dash combination after "origin_id=" and before the "&"

3. Within terminal, type in 
source_ep=<ID>
dest_ep=<ID>

4. Then, type in
 globus transfer $source_ep $dest_ep --batch <text_file.txt>
    1. text_file.txt should contain the directory list of the file directories and names within $source_ep and the file directories and names within $dest_ep, separated by a space. This is easily done through a python script. 
    2. the list of file names can be found as an attachment within the email that ARM Data Orders sends you.
