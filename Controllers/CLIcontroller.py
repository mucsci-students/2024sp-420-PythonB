#Primary: Jillian Daggs
#Secondary: Patrick McCullough
#Last Updated: 3/4/24
import os
import json
from Models.diagram import Diagram
from Models.classadd import UMLClass
import Models.attribute
from Models.saveload import SaveLoad
from Models.errorHandler import ErrorHandler


#Jill: initializes types of commands
class CLIController:
    def __init__(self, diagram, classes, fields, methods, parameters, save_load):
        self.classes = classes
        self.relationship = classes.relationships
        self.fields = fields
        self.methods = methods
        self.parameters = parameters
        self.diagram = diagram
        self.save_load = save_load
    
    def output(self, str):
        print(str)

    @ErrorHandler.handle_error
    def class_breakdown(self, name):
        '''Outputs a dictionary from from class name to fields and methods 
            (to params) for use in list class and save

        Parameters:
            name (str): The class name.

        Precondition:
            Class name must exist in classes

        Postcondition:
            None

        Returns:
            Dictionary from class name to fields and methods (to params)
        '''
        all_classes = self.classes.list_classes()
        class_list = []

        if name in all_classes: 
            fields = self.classes.classes[name]["Fields"]
            methods = self.classes.classes[name]["Methods"]
            all_methods = []

            for method in methods:
                params = methods[method]["Parameters"]
                param_list = []

                for param in params:
                    param_list.append({"name": param})

                all_methods.append({
                    "name": method,  
                    "params": param_list
                })

            class_item = {
                "name": name,
                "fields": [{"name": field} for field in fields], 
                "methods": all_methods
            }

            class_list.append(class_item)

            return class_list
        else:
            raise ValueError(f"Class, '{name}' does not exist.")
       
    @ErrorHandler.handle_error
    def add (self, tokens):
        '''All varients of add command: adds thing of type to place 

        Parameters:
            tokens (list): a list of all tokens
                token[0]: command
                token[1]: type
                token[2]: name of a class 
                token[3]: name of class (dest) OR attribute name OR method name (dest)
                token[4]: param name OR relationship type 
                

        Precondition:
            Location to add thing to must exist, thing must not already exist, thing must have a valid name

        Postcondition:
            Thing of type will be added to location. 

        Returns:
            None
        '''
        type = tokens[1].lower()
        class_name = tokens[2]
        if type == "relationship":
            if len(tokens) >= 5:
                dest = tokens[3]
                r_type = tokens[4]
                self.output( self.relationship.add_relationship(class_name,dest,r_type))
            else:
                raise ValueError("Missing arguments.")
        elif type == "class": 
            if len(tokens) >= 2:
                if self.diagram.name_checker(class_name):
                    #checks for capitalization
                    if class_name[0].isupper():
                        
                        self.output(self.classes.add_class(class_name))
                    else:
                        raise ValueError("Class names must start with capital letters.")
            else:
                raise ValueError("Missing arguments.")
        elif type == "field":
            if len(tokens) >= 4:
                class_name = tokens[2] 
                attribute_name = tokens[3]
                if self.diagram.name_checker(attribute_name):
                    self.output(self.fields.add_field(class_name, attribute_name))
            else:
                raise ValueError("Missing arguments.")
        elif type == "method":
            if len(tokens) >= 4:
                class_name = tokens[2] 
                attribute_name = tokens[3]
                if self.diagram.name_checker(attribute_name):
                    self.output(self.methods.add_method(class_name, attribute_name))
            else:
                raise ValueError("Missing arguments.")
        elif type == "parameter" or type == "param":
            if len(tokens) >= 5:
                class_name = tokens[2] 
                method_name = tokens[3] 
                attribute_name = tokens[4]
                if self.diagram.name_checker(attribute_name):
                    self.output(self.parameters.add_parameter(class_name, method_name, attribute_name))
            else:
                    raise ValueError("Missing arguments.")                                                              

    @ErrorHandler.handle_error
    def rename(self, tokens):
        '''All varients of rename command: renames 'thing' of 'type' in 'place' to 'something else' 

        Parameters:
            tokens (list): a list of all tokens
                token[0]: command
                token[1]: type
                token[2]: name of a class 
                token[3]: new name of a class OR old attribute name OR method name (dest)
                token[4]: old parameter name OR new attribute name 
                token[5]: new parameter name 

        Precondition:
            Location of 'thing' must exist, 'thing' must exist, 'something else' must have be a valid name

        Postcondition:
            'Thing' of 'type' in 'place' will be renamed to 'something else' 

        Returns:
            None
        '''        
        type = tokens[1].lower()
        classname = tokens[2]
        if type == "class":
            if len(tokens) >= 4:
                newname = tokens[3]
                if self.diagram.name_checker(newname):
                    if newname[0].isupper():                        
                        self.output(self.classes.rename_class(classname,newname))
                    else:
                        raise ValueError("Class names must start with capital letters.")
            else:
                raise ValueError ("Missing arguments.")
        elif type == "field":
            if len(tokens) >= 5:
                fieldname = tokens[3]
                newname = tokens[4]
                if self.diagram.name_checker(newname):
                    self.output(self.fields.rename_field(classname,fieldname,newname))
            else:
                raise ValueError ("Missing arguments.")
        elif type == "method":
            if len(tokens) >= 5:
                methodname = tokens[3]
                newname = tokens[4]
                if self.diagram.name_checker(newname):
                    self.output(self.methods.rename_method(classname,methodname,newname))
            else:
                raise ValueError ("Missing arguments.")
        elif type == "parameter" or type == "param":
            if len(tokens) >= 6:
                    methodname = tokens[3]
                    parametername = tokens[4]
                    newname = tokens[5]
                    if self.diagram.name_checker(newname):
                        self.output(self.parameters.rename_parameter(classname,methodname,parametername, newname))
            else:
                raise ValueError ("Missing arguments.")
            
    @ErrorHandler.handle_error
    def delete(self, tokens): 
        '''All varients of delete command: removes 'thing' of 'type' from 'place' 

        Parameters:
            tokens (list): a list of all tokens
                token[0]: command
                token[1]: type
                token[2]: name of a class 
                token[3]: name of attribute OR method name (dest) OR class name (dest)
                token[4]: parameter name
 

        Precondition:
            Location of 'thing' must exist, 'thing' must exist

        Postcondition:
            'Thing' of 'type' in 'place' will be deleted 

        Returns:
            None
        '''    
        type = tokens[1].lower()
        classname = tokens[2]
        if type == "class":
            if len(tokens) >= 3:
                self.output(self.classes.delete_class(classname))
            else:
                raise ValueError ("Missing arguments.")
        elif type == "field":
            if len(tokens) >= 4:    
                field_name = tokens[3]
                self.output(self.fields.delete_field(classname, field_name))
            else:
                raise ValueError ("Missing arguments.")
        elif type == "method":
            if len(tokens) >= 4:
                method_name = tokens[3]
                self.output(self.methods.delete_method(classname, method_name))
            else:
                raise ValueError ("Missing arguments.")
        elif type == "parameter" or type == "param":
            if len(tokens) >= 5:
                method_name = tokens[3]
                parameter_name = tokens[4]
                self.output(self.parameters.delete_parameter(classname, method_name, parameter_name))  
            else:
                raise ValueError("Missing arguments.")
        elif type == "relationship":
            if len(tokens) >= 4:
                    classname = tokens[2]
                    dest = tokens[3]
                    self.output(self.relationship.delete_relationship(classname,dest))
            else:
                raise ValueError ("Missing arguments.")

    @ErrorHandler.handle_error
    def list(self,tokens):
        '''All varients of list command 

        Parameters:
            tokens (list): a list of all tokens
                token[0]: command
                token[1]: type
                token[2]: name of a class

        Precondition:
            None

        Postcondition:
            None

        Returns:
            A visual representation of 'classes' or if applicable 'class_name'
        '''
        if len(tokens) >= 2:
            type = tokens[1]
            if type == "classes":
                all_classes = self.classes.list_classes()
                all_relationships = self.classes.relationships.list_relationships()
                classes_item = []

                for item in all_classes:
                    class_info = self.class_breakdown(item)
                    classes_item.extend(class_info)
                    
                formatted_relationships = []
                for relationship in all_relationships:
                    formatted_relationships.append({
                        "source": relationship[0],
                        "destination": relationship[1],
                        "type": relationship[2]
                    })
                        
                uml_item = {"classes" :classes_item,
                         "relationships" : formatted_relationships}                 
                return json.dumps(uml_item, indent = 2)
            elif type == "class":
                if len(tokens) >= 3:
                    name = tokens[2]
                    all_relationships = self.relationship.list_relationships()
                    class_relationships = []
                    for relationship in all_relationships:
                        if name in relationship:
                            class_relationships.append({"source": relationship[0],
                                                       "destination": relationship[1],
                                                       "type": relationship[2]})
                    class_item = {"class" : self.class_breakdown(name),
                                  "relationships" : class_relationships}
                    return json.dumps(class_item, indent = 2)
                else:
                    raise ValueError("Missing arguments.")
            elif type == "relationships" or type == "relationship":
                if len(tokens) >= 3:
                    name = tokens[2]
                    all_relationships = self.relationship.list_relationships()
                    class_relationships = []
                    for relation in all_relationships:
                        if name in relation:  # Check if name is in the list
                            class_relationships.append(relation)

                    return(class_relationships)
                else:
                    return(self.relationship.list_relationships())
        else:
            raise ValueError("Missing arguments.")

    @ErrorHandler.handle_error
    def save(self, tokens):
        '''Saves the UML diagram as a .json file in save_folder

        Parameters:
            tokens (list): a list of all tokens
                token[0]: command
                token[1]: filename

        Precondition:
            None

        Postcondition:
            There exists a file named 'filename.json' in the save folder

        Returns:
            None
        '''        
        if len(tokens) >= 2:
            name = tokens[1]
            all_classes = self.classes.list_classes()
            all_relationships = self.classes.relationships.list_relationships()
            classes_list = []  # List to store class dictionaries
            formatted_relationships = []

            # Collect information about all classes
            for item in all_classes:
                class_info = self.class_breakdown(item)
                classes_list.extend(class_info)  # Extend the list with class dictionaries

            # Format relationships
            for relationship in all_relationships:
                formatted_relationships.append({
                    "source": relationship[0],
                    "destination": relationship[1],
                    "type": relationship[2]
                })

            # Create the uml_item dictionary with all classes and relationships
            uml_item = {"classes": classes_list, "relationships": formatted_relationships}
            self.save_load.save(uml_item, name)

        elif len(tokens) <= 1:
            raise ValueError("No filename provided.")



    @ErrorHandler.handle_error
    def load(self, tokens):
        '''Loads a UML diagram from a .json file in save_folder

        Parameters:
            tokens (list): a list of all tokens
                token[0]: command
                token[1]: filename

        Precondition:
            There exists a file named 'filename.json' in the save folder

        Postcondition:
            The contents of the file are now in their appropriate locations

        Returns:
            None
        '''    
        save_folder = 'save_folder'

        if len(tokens) >= 2:
            name = tokens[1]

            file_path = os.path.join(save_folder, name + ".json")

            if not os.path.exists(file_path):
                raise ValueError(f"File, '{file_path}' does not exist.")
            # Protects against loading a file that does not exist. (2/15/24)

            else:
                save_item = self.save_load.load(name)
                for class_item in save_item["classes"]:
                    class_name = class_item["name"] 
                    self.add(["add","class", class_name])
                    for field in class_item["fields"]:
                        self.add(["add","field", class_name, field["name"]])
                    for method in class_item["methods"]:
                        self.add(["add", "method", class_name, method["name"]])
                        for param in method["params"]:
                            self.add(["add","parameter", class_name, method["name"], param["name"]])
            for relation in save_item["relationships"]:
                src = relation["source"]
                dest = relation["destination"]
                type = relation["type"]
                self.add(["add", "relationship",src, dest, type])
                   

        else:
            raise ValueError("No filename provided.")


diagram = Diagram()
classes = UMLClass(diagram)
fields = Models.attribute.Fields(classes)
methods = Models.attribute.Methods(classes)
parameters = Models.attribute.Parameters(methods)
saveload = SaveLoad()


