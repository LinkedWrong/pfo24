<script lang="ts">
	let promise: Promise<void> | undefined = $state();

	let files_users: FileList | undefined = $state();
	let files_transactions: FileList | undefined = $state();

	$inspect(files_users).with(console.log);
	$inspect(files_transactions).with(console.log);

	async function handleSubmit() {
		if (!files_users?.length || !files_transactions?.length) {
			(document.getElementById('alert_dialog') as HTMLDialogElement).showModal();
			return;
		}

		let formData = new FormData();
		formData.append('users_file', files_users[0]);
		formData.append('transactions_file', files_transactions[0]);

		(document.getElementById('my_modal_1') as HTMLDialogElement).showModal();
		promise = fetch('http://localhost:8000/', {
			method: 'POST',
			body: formData
		})
			.then((res) => res.blob())
			.then((blob) => {
				var file = window.URL.createObjectURL(blob);
				window.location.assign(file);
			});
	}
</script>

<!--
<div class="card fixed bottom-2 right-2 z-50 flex md:bottom-4 md:right-4">
</div> -->

<dialog id="alert_dialog" class="modal">
	<div class="modal-box">
		<h3 class="text-lg font-bold">Ошибка: не все поля заполнены</h3>
		<p>Пожалуйста, заполните все поля</p>
		<div class="modal-action">
			<form method="dialog">
				<button class="btn">Закрыть</button>
			</form>
		</div>
	</div>
</dialog>

<dialog id="my_modal_1" class="modal">
	<div class="modal-box">
		<h3 class="text-lg font-bold">Fetch result</h3>
		{#if promise}
			{#await promise}
				<span class="loading loading-spinner loading-lg"></span>
			{:then}
				<p>Готово</p>
			{:catch error}
				<p style="color: red">{error.message}</p>
			{/await}
		{/if}

		<div class="modal-action">
			<form method="dialog">
				<button class="btn">Закрыть</button>
			</form>
		</div>
	</div>
</dialog>

<nav>
	<div class="navbar bg-base-300">
		<div class="navbar-start">
			<a class="btn btn-ghost text-xl">Прогнозирование раннего выхода на пенсию</a>
		</div>
		<div class="navbar-end">
			<p class="hidden md:block">
				Ключевая ставка ЦБ на 27.10.24: 21% <br />
				Официальный курс доллара: 96.67 рублей<br />
				Официальный уровень инфляции: 7.42%
			</p>
		</div>
	</div>
</nav>

<main
	class="mx-auto mt-0 flex max-w-[1200px] flex-col p-4 transition-all duration-300 ease-in-out md:p-14"
>
	<!-- <p class="mb-8 text-xl font-semibold">Прогнозирование раннего выхода на пенсию</p> -->

	<div class="mx-auto flex w-full items-center justify-center">
		<p class="text-lg font-medium">
			Предложенное решение представляет собой прототип сервиса, который прогнозирует вероятность
			досрочного выхода на пенсию для клиентов ОПС. Сервис анализирует характеристики клиента и
			текущие макроэкономические показатели, чтобы предсказать, обратится ли он за досрочной
			пенсией.
		</p>
	</div>
	<div class="divider"></div>
	<div class="container mx-auto flex h-full w-full max-w-[600px] items-center justify-center">
		<div class="roundex-2xl max-w-max-w-[500px] card w-full bg-neutral-content shadow-xl">
			<div class="card-body">
				<h2 class="card-title">Загрузить файлы</h2>
				<!-- <div class="divider"></div> -->
				<label for="users_file">Выберите файл с данными о пользователях</label>
				<input
					id="users_file"
					type="file"
					class="file-input file-input-bordered mb-4 mt-1 w-full"
					bind:files={files_users}
				/>
				<!-- <div class="divider"></div> -->

				<label for="transactions_file">Выберите файл с данными о транзакциях</label>
				<input
					id="transactions_file"
					type="file"
					class="file-input file-input-bordered mt-1 w-full"
					bind:files={files_transactions}
				/>

				<div class="divider"></div>
				<button
					onclick={handleSubmit}
					class="btn card-body disabled btn-primary rounded-xl"
					class:btn-disabled={!files_users?.length || !files_transactions?.length}
				>
					Отправить
				</button>
			</div>
		</div>
	</div>
	<div class="divider"></div>
	<!-- <div class="divider divider-horizontal"></div> -->
</main>
