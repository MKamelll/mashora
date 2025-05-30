<script>
	import FatherInfo from './../lib/components/FatherInfo.svelte';
    import MotherInfo from "$lib/components/MotherInfo.svelte";
	import ChildInfo from '$lib/components/ChildInfo.svelte';
	let tab = 'mother';
</script>

<div>
	<div class="tabs mb-4">
		<a class="tab" class:tab-active={tab === 'mother'} on:click={() => tab = 'mother'}>بيانات الأم</a>
		<a class="tab" class:tab-active={tab === 'father'} on:click={() => tab = 'father'}>بيانات الأب</a>
        <a class="tab" class:tab-active={tab === 'child'} on:click={() => tab = 'child'}>بيانات الطفل</a>
        <a class="tab" class:tab-active={tab === 'breast-feeding'} on:click={() => tab = 'breast-feeding'}>معلومات الرضاعة وقت الزيارة</a>
        <a class="tab" class:tab-active={tab === 'visit-topics'} on:click={() => tab = 'visit-topics'}>مواضيع الزيارة</a>
        <a class="tab" class:tab-active={tab === 'visit-notes'} on:click={() => tab = 'visit-notes'}>ملاحاظات الزيارة</a>
        <a class="tab" class:tab-active={tab === 'next-visit-plan'} on:click={() => tab = 'breast-feeding'}>خطة الزيارة القادمة</a>
	</div>

	{#if tab === 'mother'}
		<MotherInfo/>
    {:else if tab == 'father'}
        <FatherInfo/>
    {:else if tab == 'child'}
        <ChildInfo/>
	{/if}
</div>
