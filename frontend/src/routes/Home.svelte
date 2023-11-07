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

    let question_list = []
    let size = 10
    let page = 0
    let total = 0
    $: total_page = Math.ceil(total/size)

    function get_question_list(_page) {
        let params = {
            page: _page,
            size: size,
        }
        fastapi('get', '/api/question/list', params, (json) => {
            question_list = json.question_list
            page = _page
            total = json.total
        })
    }

    get_question_list(0)
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
        <tr class="table-dark">
            <th>번호</th>
            <th>제목</th>
            <th>작성일시</th>
        </tr>
        </thead>
        <tbody>
        {#each question_list as question, i}
        <tr>
            <td>{i+1}</td>
            <td>
                <a use:link href="/detail/{question.id}">{question.subject}</a>
            </td>
            <td>{question.create_date}</td>
        </tr>
        {/each}
        </tbody>
    </table>
    <!-- 페이징처리 시작 -->
    <ul class="pagination justify-content-center">
        <!-- 이전페이지 -->
        <li class="page-item {page <= 0 && 'disabled'}">
            <button class="page-link" on:click="{() => get_question_list(page-1)}">이전</button>
        </li>
        <!-- 페이지번호 -->
        {#each Array(total_page) as _, loop_page}
        <li class="page-item {loop_page === page && 'active'}">
            <button on:click="{() => get_question_list(loop_page)}" class="page-link">{loop_page+1}</button>
        </li>
        {/each}
        <!-- 다음페이지 -->
        <li class="page-item {page >= total_page-1 && 'disabled'}">
            <button class="page-link" on:click="{() => get_question_list(page+1)}">다음</button>
        </li>
    </ul>
    <!-- 페이징처리 끝 -->
    <a use:link href="/question-create" class="btn btn-primary">질문 등록하기</a>
</div>