<!-- <script>
    import fastapi from "../lib/api"
    import { link } from 'svelte-spa-router'

    let question_list = []

    function get_question_list() {
        // fetch("http://127.0.0.1:8000/api/question/list").then((response) => {
        //     response.json().then((json) => {
        //         question_list = json
        //     })
        // })

        fastapi('get', '/api/question/list', {}, (json) => {
            question_list = json
        })
        // 화살표 함수 내용 : 응답으로 받은 json 데이터를 question_list에 대입하라
    }

    get_question_list()
</script> -->

<!-- 게시판 페이징 적용 -->
<script>
    import fastapi from "../lib/api"
    import { link } from 'svelte-spa-router'
    import { page, is_login } from "../lib/store" // 스토어를 사용하여 page를 전역변수로
    import moment from 'moment/min/moment-with-locales'
    moment.locale('ko')

    let question_list = []
    let size = 10
    //let page = 0 // 스토어 변수로 바꾸어 주었기 때문에 삭제한다.
    let total = 0
    $: total_page = Math.ceil(total/size)
    // $: Svelte의 reactive assignment 문법으로 변수를 리액티브하게 업데이트

    function get_question_list(_page) {
        let params = {
            page: _page,
            size: size,
        }
        fastapi('get', '/api/question/list', params, (json) => {
            question_list = json.question_list
            $page = _page // $을 붙여서 동적변수로 지정
            total = json.total
        })
    }

    // $: 기호는 변수 뿐만 아니라 함수나 구문 앞에 추가하여 사용할 수 있다. 
    // page 값이 변경될 경우 get_question_list 함수도 다시 호출하라는 의미
    $: get_question_list($page)
</script>

<!-- 
<ul>
    {#each question_list as question}
        <li>{question.subject}</li> 
        <li><a use:link href="/detail/{question.id}">{question.subject}</a></li>
    {/each}
</ul>
-->

<!-- 
    부트스트랩 적용 : 
        class="container my-3", 
        class="table", 
        class="table-dark" 
        등의 클래스가 부트스트랩이 제공하는 클래스이다,
-->

<div class="container my-3">
    <table class="table">
        <thead>
        <tr class="text-center table-dark">
            <th>번호</th>
            <th style="width:50%">제목</th>
            <th>글쓴이</th>
            <th>작성일시</th>
        </tr>
        </thead>
        <tbody>
            {#each question_list as question, i}
            <tr class="text-center">
                <td>{ total - ($page * size) - i }</td>
                <td class="text-start">
                    <a use:link href="/detail/{question.id}">{question.subject}</a>
                    {#if question.answers.length > 0 }
                    <span class="text-danger small mx-2">{question.answers.length}</span>
                    {/if}
                </td>
                <td>{ question.user ? question.user.username : "" }</td>
                <td>{moment(question.create_date).format("YYYY년 MM월 DD일 hh:mm a")}</td>
            </tr>
            {/each}
        </tbody>
    </table>
    <!-- 페이징처리 시작 -->
    <ul class="pagination justify-content-center">
        <!-- 이전페이지 -->
        <li class="page-item {$page <= 0 && 'disabled'}">
            <button class="page-link" on:click="{() => get_question_list($page-1)}">이전</button>
        </li>
        <!-- 페이지번호 -->
        {#each Array(total_page) as _, loop_page}
        {#if loop_page >= $page-5 && loop_page <= $page+5} 
        <li class="page-item {loop_page === $page && 'active'}">
            <button on:click="{() => get_question_list(loop_page)}" class="page-link">{loop_page+1}</button>
        </li>
        {/if}
        {/each}
        <!-- 다음페이지 -->
        <li class="page-item {$page >= total_page-1 && 'disabled'}">
            <button class="page-link" on:click="{() => get_question_list($page+1)}">다음</button>
        </li>
    </ul>
    <!-- 페이징처리 끝 -->
    <a use:link href="/question-create" class="btn btn-primary {$is_login ? '' : 'disabled'}">질문 등록하기</a>
</div>