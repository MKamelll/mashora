<form class="grid grid-cols-1 md:grid-cols-2 gap-6 bg-base-200 p-6 rounded-lg shadow">
    <div>
        <label class="label">
            <span class="label-text">الاسم</span>
        </label>
        <input type="text" class="input input-bordered w-full"  />
    </div>
    <div>
        <label class="label">
            <span class="label-text">الرقم القومي</span>
        </label>
        <input type="text" inputmode="numeric" pattern="[0-9]" class="input input-bordered w-full no-spinner" placeholder="تأكد من كتابة 14 رقم" />
    </div>
    <div>
        <label class="label">
            <span class="label-text">رقم الهاتف</span>
        </label>
        <input type="tel" class="input input-bordered w-full" placeholder="تأكد من كتابة 11 رقم"/>
    </div>
    <div>
        <label class="label">
            <span class="label-text"> مستوي تعليم الأب</span>
        </label>
        <select class="select select-bordered w-full">
            <option value="none">أمي</option>
            <option value="can-read">يجيد القراءة</option>
            <option value="moderate">مؤهل متوسط</option>
            <option value="above-moderate">فوق المتوسط</option>
            <option value="excellant">مؤهل عالي</option>
        </select>
    </div>
    <div>
        <label class="label">
            <span class="label-text"> الوظيفة</span>
        </label>
        <select class="select select-bordered w-full">
            <option value="work">يعمل</option>
            <option value="doesnot-work">لا يعمل</option>
        </select>
    </div>
    <div class="md:col-span-2 text-right flex justify-end">
        <button class="btn btn-primary">متابعة</button>
    </div>
</form>