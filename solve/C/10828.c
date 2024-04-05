#include <stdio.h>
#include <stdlib.h>

// 스택의 각 요소를 나타내는 Node 구조체 정의
typedef struct Node {
    int data;           // 해당 노드에 저장되는 데이터
    struct Node *link;  // 다음 노드를 가리키는 포인터
} Node;

// 스택 자체를 나타내는 Stack 구조체 정의
typedef struct {
    Node *top;  // 스택의 맨 위에 있는 노드를 가리키는 포인터
} Stack;

// 스택을 초기화하는 init() 함수. 매개변수로 스택을 받아와서 스택을 초기화 한다.
void init(Stack *s)
{
    s->top = NULL;
}

// 스택이 비어 있는지 여부를 확인하는 함수
int is_empty(Stack *s)
{
    return (s->top == NULL);
}

// 스택에 새로운 요소를 추가하는 함수
void push(Stack *s, int item)
{
    Node *temp = (Node *)malloc(sizeof(Node)); // 새로운 노드를 동적으로 할당
    temp->data = item; // 새로운 노드에 입력할 값 복사
    temp->link = s->top; // 새로운 노드가 기존의 top 노드를 가리키도록 함
    s->top = temp; // 새로운 노드가 top 노드로 선언
}

// 스택에서 요소를 제거하는 함수
int pop(Stack *s)
{
    if(is_empty(s)){ // 스택이 비어 있는지 확인
        return -1; // 스택이 비어있으면 -1 반환
    }
    else{
        Node *temp = s->top; // temp포인터를 top노드를 가르키도록 함
        int data = temp->data; // 삭제한 값 반환하기 위해서 기존의 데이터를 temp노드에 삽입
        s->top = s->top->link; // top 노드는 기존의 top노드가 가르키는 노드가 됨
        free(temp); // 동적 메모리 해제
        return data; // 삭제할 값 반환
    }
}

// 스택의 내용을 출력하는 함수
void print_stack(Stack *s)
{
    if(is_empty(s)) {
        printf("-1\n");
        return;
    }

    for(Node *p = s->top; p != NULL; p = p->link)
        printf("%d ", p->data);
    printf("\n");
}

int main()
{
    Stack s;
    init(&s); // 스택 초기화

    int N;
    scanf("%d", &N); // 명령의 수 입력 받기

    while(N--) {
        char cmd[10];
        scanf("%s", cmd);

        if(strcmp(cmd, "push") == 0) {
            int X;
            scanf("%d", &X);
            push(&s, X);
        }
        else if(strcmp(cmd, "pop") == 0) {
            printf("%d\n", pop(&s));
        }
        else if(strcmp(cmd, "size") == 0) {
            int count = 0;
            for(Node *p = s.top; p != NULL; p = p->link)
                count++;
            printf("%d\n", count);
        }
        else if(strcmp(cmd, "empty") == 0) {
            printf("%d\n", is_empty(&s));
        }
        else if(strcmp(cmd, "top") == 0) {
            if(is_empty(&s))
                printf("-1\n");
            else
                printf("%d\n", s.top->data);
        }
    }

    return 0;
}