<template>
  <div class="legends">
    <div v-for="{name, color} in legends" :key="name" class="legends__item">
      <div :style="`--mark-color: ${color};`" class="legends__mark" />
      <span class="legends__label">{{ name }}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BaseLegends',
  props: {
    legends: {type: Array, default: () => [{name: '', color: ''}]},
  },
}
</script>

<style lang="scss" scoped>
.legends {
  position: absolute;
  top: calc(100% + 20px);

  display: flex;
  justify-content: center;

  gap: 12px;
  widows: 100%;

  &__item {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  &__mark {
    width: 20px;
    height: 10px;
    background-color: var(--mark-color);
  }

  &__label {
    font-size: 12px;
    color: var(--typography-secondary-color);
  }
}
</style>
