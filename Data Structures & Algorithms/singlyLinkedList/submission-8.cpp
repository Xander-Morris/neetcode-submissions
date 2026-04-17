class Node {
public:
    Node(int value, Node* next) {
        this->value = value;
        this->next = next;
    }

    void set_next(Node* next) {
        this->next = next;
    }

    void set_value(int value) {
        this->value = value;
    }

    Node* get_next() {
        return this->next;
    }

    int get_value() {
        return this->value;
    }

private:
    int value;
    Node* next;
};

class LinkedList {
private:
    Node* head = NULL;

public:
    LinkedList() {

    }

    int get(int index) {
        if (index == 0) { return head != NULL ? head->get_value() : -1; }
        int i = 0;
        Node* temp = head;

        while (temp != NULL) {
            temp = temp->get_next();
            i++;
            if (i == index && temp != NULL) { return temp->get_value(); }
        }

        return -1;
    }

    void insertHead(int val) {
        if (head == NULL) {
            head = new Node(val, NULL);
        } else {
            Node* new_node = new Node(val, NULL);
            new_node->set_next(head);
            head = new_node;
        }
    }
    
    void insertTail(int val) {
        if (head == NULL) { 
            head = new Node(val, NULL); 
            return; 
        }

        Node* temp = head;
        while (temp->get_next() != NULL) {
            temp = temp->get_next();
        }

        Node* new_node = new Node(val, NULL);
        temp->set_next(new_node);
    }

    bool remove(int index) {
        if (head == NULL) { return false; }
        Node* temp = head;

        if (index == 0) {
            head = head->get_next();
            delete temp;
            return true;
        }

        int i = 0;
        Node* previous = NULL;
        while (temp->get_next() != NULL) {
            previous = temp;
            temp = temp->get_next();
            i++;

            if (i == index && temp != NULL) {
                previous->set_next(temp->get_next());
                delete temp;
                return true;
            }
        }

        return false;
    }

    vector<int> getValues() {
        vector<int> values;
        Node* temp = head;

        while (temp != NULL) {
            values.push_back(temp->get_value());
            temp = temp->get_next();
        }

        return values;
    }
};
