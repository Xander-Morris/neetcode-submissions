type MyCircularQueue struct {
    q[] int 
	k int 
}


func Constructor(k int) MyCircularQueue {
    return MyCircularQueue{
		q: []int{},
		k: k,
	}
}


func (this *MyCircularQueue) EnQueue(value int) bool {
    if (len(this.q) >= this.k) {
		return false;
	}

	this.q = append(this.q, value)
	return true;
}


func (this *MyCircularQueue) DeQueue() bool {
    if (len(this.q) == 0) {
		return false;
	}

	this.q = this.q[1:]
	return true;
}


func (this *MyCircularQueue) Front() int {
    if len(this.q) > 0 {
		return this.q[0]
	}

	return -1
}


func (this *MyCircularQueue) Rear() int {
    if len(this.q) > 0 {
		return this.q[len(this.q) - 1]
	}

	return -1
}

func (this *MyCircularQueue) IsEmpty() bool {
    return len(this.q) == 0
}

func (this *MyCircularQueue) IsFull() bool {
    return len(this.q) >= this.k
}


/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * obj := Constructor(k);
 * param1 := obj.EnQueue(value);
 * param2 := obj.DeQueue();
 * param3 := obj.Front();
 * param4 := obj.Rear();
 * param5 := obj.IsEmpty();
 * param6 := obj.IsFull();
 */
 