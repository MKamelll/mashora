<script>
    let followup_place_selected = '';
    let referal_source = '';
</script>

<form class="grid grid-cols-1 md:grid-cols-2 gap-6 bg-base-200 p-6 rounded-lg shadow">
    <div>
        <label class="label">
            <span class="label-text">الاسم</span>
        </label>
        <input type="text" class="input input-bordered w-full"  />
    </div>
    <div>
        <label class="label">
            <span class="label-text">تاريخ الميلاد</span>
        </label>
        <input type="date" class="input input-bordered w-full" />
    </div>
    <div>
        <label class="label">
            <span class="label-text">العمر الحالي للطفل</span>
        </label>
        <input type="text" inputmode="numeric" pattern="[0-9]" class="input input-bordered w-full no-spinner" placeholder="بالشهور"/>
    </div>

    <div>
        <label class="label">
            <span class="label-text">العمر الرحمي للطفل</span>
        </label>
        <input type="text" inputmode="numeric" pattern="[0-9]" class="input input-bordered w-full no-spinner" placeholder="بالاسبوع"/>
    </div>

    <div>
        <div>
            <label class="label">
                <span class="label-text">مكان المتابعة</span>
            </label>
            <select class="select select-bordered w-full" bind:value={followup_place_selected}>
                <option value="unit">وحدة</option>
                <option value="hospital">مستشفي</option>
                <option value="other">اخري</option>
            </select>
        </div>
        
        {#if followup_place_selected !== ''}
            {#if followup_place_selected === 'unit'}
                <div>
                    <input type="text" class="input input-bordered w-full" placeholder="ادخل اسم الوحدة" />
                </div>
            {:else if followup_place_selected == 'hospital'}
                <div>
                    <input type="text" class="input input-bordered w-full" placeholder="ادخل اسم المستشفي" />
                </div>
            {:else}
                <div>
                    <input type="text" class="input input-bordered w-full" placeholder="ادخل اسم المكان" />
                </div>
            {/if}
        {/if}
        
    </div>

    <div>
        <div>
            <label class="label">
                <span class="label-text"> مصدر الاحالة</span>
            </label>
            <select class="select select-bordered w-full" bind:value={referal_source}>
                <option value="hospital">مستشفي</option>
                <option value="clinic">عيادة خاصة</option>
                <option value="vaccine-clinic">عيادة التطعيمات</option>
                <option value="advice">نصيحة</option>
            </select>
        </div>
        
        {#if referal_source !== ''}
            {#if referal_source === 'hospital'}
                <div>
                    <input type="text" class="input input-bordered w-full" placeholder="ادخل اسم المستشفي" />
                </div>
            {:else if referal_source === 'clinic'}
                <div>
                    <input type="text" class="input input-bordered w-full" placeholder="ادخل اسم العيادة الخاصة" />
                </div>
            {/if}
        {/if}
        
    </div>

    <div class="md:col-span-2 text-right flex justify-end">
        <button class="btn btn-primary">متابعة</button>
    </div>
</form>