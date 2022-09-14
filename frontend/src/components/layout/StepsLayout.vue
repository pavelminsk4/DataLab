<template>
  <div class="steps-layout-wrapper">
    <slot name="navigation"></slot>

    <slot name="form"></slot>
  </div>
</template>

<script>
export default {
  name: 'StepsLayout',
}
</script>
