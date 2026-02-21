const tierButton = document.getElementById('tier-btn');
const offerTitle = document.getElementById('offer-title');
const offerSub = document.getElementById('offer-sub');

const offers = {
  A: ['年费会员 + Pro 硬件组合包 + 延保', '适合高价值用户，优先提升 LTV'],
  B: ['月费会员 + 限时硬件券', '中价值用户优先拉动首购'],
  C: ['7天体验包 + 低价 IAP 程序', '低门槛回流，降低流失'],
};

let index = 0;
const tiers = ['A', 'B', 'C'];

tierButton.addEventListener('click', () => {
  index = (index + 1) % tiers.length;
  const tier = tiers[index];
  tierButton.textContent = `${tier}层用户`;
  offerTitle.textContent = offers[tier][0];
  offerSub.textContent = offers[tier][1];
});
