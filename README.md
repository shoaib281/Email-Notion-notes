# Email-Notion-notes
_Program that emails random notes from notion to you_

#### Installation instructions

1. Download this repo as a zip file
2. Unzip the file 
3. Provide sender and receiver email address
4. Provide notion page [link](https://www.alphr.com/how-to-link-to-another-page-notion/)
5. Provide your notion [token](https://peopleleaders.io/How-to-get-Notion-Token-and-Workspace-IDs-11e67f9733d545fcb83f3dba0b149f5b)
6. Input your email address password

### Structuring your notion page

Have a master notion block page that contains all the pages which contain your notes.

Only notion pages after the first divider block get selected so ensure that all the notes you want emailed are after the first divider block.

Your notes should be stored inside of these subpages. It should be [noted](https://tenor.com/view/badumtss-baxmusic-bax-shop-bax-it-gif-14812059) that all notes that you want to be emailed should be bullet points so that headings and titles don't get emailed. 

### Notes that get emailed

By default 3 notes will be emailed but this can be changed in the `values.json` file that accompanies this program.

All the required information stated above, except for the Sender E-Mail Password can be changed by directly editting the `values.json` file.

If no values are given for the required information, at the beginning of the program, the program asks for that information which will then be stored.

### Scheduling daily emails

The program is best used with windows task [scheduler](https://www.windowscentral.com/how-create-automated-task-using-task-scheduler-windows-10) and to specifically schedule python files see [here](https://stackoverflow.com/questions/44727232/scheduling-a-py-file-on-task-scheduler-in-windows-10)

### Show your support

Follow me on Twitter [@iamshabbs15](https://twitter.com/iamshabbs15), for updates, you can contact me there as well
