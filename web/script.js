function drawCard(data) {
    const canvas = document.getElementById('cardCanvas');
    const ctx = canvas.getContext('2d');
    canvas.style.display = 'block';

    // background
    ctx.fillStyle = '#ffffff';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = '#000000';
    ctx.font = '16px sans-serif';
    const lines = [
        `아이 이름: ${data.child_name}`,
        `생년월일: ${data.birth_date}`,
        `혈액형: ${data.blood_type}`,
        `지병: ${data.diseases}`,
        `알러지: ${data.allergies}`,
        `특이사항: ${data.special_notes}`,
        `부모 연락처: ${data.parent_contact}`,
        `긴급 연락처: ${data.emergency_contact}`
    ];

    let y = 30;
    lines.forEach(line => {
        ctx.fillText(line, 20, y);
        y += 30;
    });

    const downloadArea = document.getElementById('downloadArea');
    const link = document.getElementById('downloadLink');
    link.href = canvas.toDataURL('image/png');
    downloadArea.style.display = 'block';
}

function gatherData() {
    const form = document.getElementById('cardForm');
    return {
        child_name: form.querySelector('#child_name').value,
        birth_date: form.querySelector('#birth_date').value,
        blood_type: form.querySelector('#blood_type').value,
        diseases: form.querySelector('#diseases').value,
        allergies: form.querySelector('#allergies').value,
        special_notes: form.querySelector('#special_notes').value,
        parent_contact: form.querySelector('#parent_contact').value,
        emergency_contact: form.querySelector('#emergency_contact').value
    };
}

document.getElementById('generate').addEventListener('click', () => {
    drawCard(gatherData());
});
