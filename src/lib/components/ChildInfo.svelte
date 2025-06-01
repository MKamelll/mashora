<script>
    let followup_place_selected = '';
    let referal_source = '';
    let delivery_type = '';
    let delivery_place = '';
    let baby_hospitalization = '';
    let reason_for_baby_hospitalization = '';
    let skin_to_skin_contact_during_first_hour = '';
    let breast_feeding_during_first_hour = '';
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

    <div>
        <label class="label">
            <span class="label-text">نوع الولادة</span>
        </label>
        <select class="select select-bordered w-full" bind:value={delivery_type}>
            <option value="c-section">قيصري</option>
            <option value="non-c-section">طبيعي</option>
        </select>
    </div>

    <div>
        <label class="label">
            <span class="label-text">مكان الولادة</span>
        </label>
        <select class="select select-bordered w-full" bind:value={delivery_place}>
            <option value="home">المنزل</option>
            <option value="hospital">المستشفي</option>
        </select>
    </div>

    <div>
        <label class="label">
            <span class="label-text">وزن الطفل عند الولادة</span>
        </label>
        <input type="text" inputmode="numeric" pattern="[0-9]" class="input input-bordered w-full no-spinner" placeholder="بالكيلوجرام"/>
    </div>

    <div>
        <label class="label">
            <span class="label-text">طول الطفل عند الولادة</span>
        </label>
        <input type="text" inputmode="numeric" pattern="[0-9]" class="input input-bordered w-full no-spinner" placeholder="بالسنتيمتر"/>
    </div>

    <div>
        <label class="label">
            <span class="label-text">مقاس راس الطفل عند الولادة</span>
        </label>
        <input type="text" inputmode="numeric" pattern="[0-9]" class="input input-bordered w-full no-spinner" placeholder="بالسنتيمتر"/>
    </div>

    <div>
        <div>
            <label class="label">
                <span class="label-text">دخول الحضانة</span>
            </label>
            <select class="select select-bordered w-full" bind:value={baby_hospitalization}>
                <option value="yes">تم</option>
                <option value="no">لم يتم</option>
            </select>
        </div>
    
        {#if baby_hospitalization !== ''}
            {#if baby_hospitalization === 'yes'}
                <div>
                    <label class="label">
                        <span class="label-text">سبب دخول الحضانة</span>
                    </label>
                    <select class="select select-bordered w-full" bind:value={reason_for_baby_hospitalization}>
                        <option value="below-average-weight">انخفاض وزن الطفل</option>
                        <option value="need-for-medication">احتياج الطفل لأدوية محددة بهذا الوقت</option>
                        <option value="difficulty-breathing">صعوبة شديدة في التنفس لعدم اكتمال نمو الرئتين</option>
                        <option value="fever">ارتفاع درجة حرارة جسم الرضيع</option>
                        <option value="abnormal-vital-signs">تعطل العمليات الحيوية بجسم الطفل</option>
                        <option value="hypoglycemia">انخفاض معدل الجلوكوز في دم الطفل</option>
                        <option value="abnormal-git-function">معاناة الرضيع مشكلات في الجهاز الهضمي</option>
                        <option value="septicemia">اصابة الطفل بعدوي في الدم</option>
                        <option value="jaundice">اصابة الطفل بالصفراء</option>
                        <option value="problems-during-pregnancy">حدوث مشكلات خلال الولادة "الولادة المتعسرة أو الحمل الحرج"</option>
                        <option value="birth-defect">وجود عيب خلقي يمنع الطفل عن التنفس أو الرضاعة بشكل طبيعي</option>
                    </select>
                </div>
            {/if}
        {/if}
    </div>

    <div>
        <label class="label">
            <span class="label-text">مدة البقاء في الحضانة</span>
        </label>
        <input type="text" inputmode="numeric" pattern="[0-9]" class="input input-bordered w-full no-spinner" placeholder="بالأيام"/>
    </div>

    <div>
        <label class="label">
            <span class="label-text">ملامسة الجلد في الساعة الذهبية الأولي</span>
        </label>
        <select class="select select-bordered w-full" bind:value={skin_to_skin_contact_during_first_hour}>
            <option value="yes">تم</option>
            <option value="no">لم يتم</option>
        </select>
    </div>

    <div>
        <label class="label">
            <span class="label-text">الرضاعة الطبيعية في الساعة الذهبية الأولي</span>
        </label>
        <select class="select select-bordered w-full" bind:value={breast_feeding_during_first_hour}>
            <option value="yes">تم</option>
            <option value="no">لم يتم</option>
        </select>
    </div>

    <div class="md:col-span-2 text-right flex justify-end">
        <button class="btn btn-primary">متابعة</button>
    </div>
</form>