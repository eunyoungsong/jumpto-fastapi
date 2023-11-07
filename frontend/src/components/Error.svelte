<script>
    export let error  // 전달받은 오류
</script>

{#if typeof error.detail === 'string'}
<!-- 부트스트랩의 Alerts 컴포넌트를 사용하여 오류가 예쁘게 표시되도록 수정 -->
    <div class="alert alert-danger" role="alert">
        <div>
            {error.detail}
        </div>
    </div>
{:else if typeof error.detail === 'object' && error.detail.length > 0 }
    <div class="alert alert-danger" role="alert">
        {#each error.detail as err, i}
        <div>
            <strong>{err.loc[1]}</strong> : {err.msg}
        </div>
        {/each}
    </div>
{/if}
