//usually trie ds.
//each node
class Node{

    constructor(){

        this.children = {};
        this.is_last_chr = false;
        this.repeat_char = -1;
    }
}

//complete tree like structure this is called one time complete trie
class Structure{
    constructor(){
        this.root = new Node();
        //word list to be returned for the suggestion tasks :
        this.word_list = [];
    }
    //form the trie ds
    formStructure = (all_keys) =>{

        for(var i=0;i<all_keys.length;i++){
            this.insert(all_keys[i]);
        }
    }
    //insert in the structure if it not already presents .param is option

    insert = (k) =>{

            var node = this.root;
            for(var i=0;i<k.length;i++){

                if(!node.children[k[i]]){
                        node.children[k[i]]= new Node();
                }
                node = node.children[k[i]];
            }

            node.is_last_chr = true;
            console.log(`hence ${k} is inserted`);
    }
    //full match of the key return true on success
    search = (key) =>{
            var node = this.root;
            var found = true;
            for(var i=0;i<key.length;i++){
                if(!node.children[key[i]])
                {
                    found=false;
                    break;
                }
                node = node.children[key[i]]

        }

        return node && node.is_last_chr && found

    }

}

//testing 
keys = ['hello','hel','helping','dog','hi']
search = 'hi'


structure = new Structure();
structure.formStructure(keys);
bool = structure.search(search);
console.log(bool);
