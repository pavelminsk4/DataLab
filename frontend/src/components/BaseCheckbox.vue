<template>
  <label class="container container-header">
    <input type="checkbox" />
    <span class="checkmark">
      <CheckRadioIcon class="checkmark-icon" />
    </span>
    <div class="title"><slot></slot></div>
  </label>
</template>

<script>
import CheckRadioIcon from '@components/icons/CheckIcon'

export default {
  name: 'BaseCheckbox',
  components: {
    CheckRadioIcon,
  },
}
</script>

<style scoped>
.container {
  position: relative;

  display: block;

  font-size: 22px;

  cursor: pointer;

  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.container input {
  position: absolute;

  height: 0;
  width: 0;

  opacity: 0;
  cursor: pointer;
}

.checkmark {
  top: 0;
  left: 0;

  display: flex;
  align-items: center;
  justify-content: center;

  height: 20px;
  width: 20px;

  border: 1px solid var(--secondary-text-color);
  border-radius: 4px;
  background-color: var(--input-border-color);
}

.title {
  margin-left: 27px;

  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
  color: var(--primary-text-color);
}

.container:hover input ~ .checkmark {
  background-color: var(--secondary-bg-color);
}

.container input:checked ~ .checkmark {
  border: none;
  background-color: var(--primary-button-color);
}

.container input ~ .checkmark > .checkmark-icon {
  display: none;
}

.container input:checked ~ .checkmark > .checkmark-icon {
  display: block;
}

.container input:checked ~ .checkmark:after {
  display: block;
}
</style>
