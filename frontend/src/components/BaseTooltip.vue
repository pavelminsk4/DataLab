<template>
  <div class="options-container">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: 'BaseTooltip',
}
</script>

<style lang="scss" scoped>
.options-container {
  position: absolute;
  right: 40px;

  display: flex;
  flex-direction: column;

  white-space: nowrap;

  border-radius: 4px;
  padding: 10px 15px;
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.22);

  background: var(--typography-primary-color);

  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 110%;
  color: var(--secondary-button-color);

  &::after {
    content: '';

    position: absolute;
    top: 29%;
    right: -10px;

    transform: translate(-50%, -50%) rotate(225deg);

    margin-left: 2px;

    border-width: 5px;
    border-style: solid;
    border-bottom-left-radius: 2px;

    color: var(--typography-primary-color);
  }
}
</style>
