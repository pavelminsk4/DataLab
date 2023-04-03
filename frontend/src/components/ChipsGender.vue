<template>
  <div :class="['wrapper', genderType]">
    <component :is="`${genderType}Icon`" />
    <span>{{ capitalizeFirstLetter(genderType) }}</span>
  </div>
</template>

<script>
import {capitalizeFirstLetter} from '@/lib/utilities'

import maleIcon from '@/components/icons/MaleIcon'
import femaleIcon from '@/components/icons/FemaleIcon'

export default {
  components: {maleIcon, femaleIcon},
  props: {
    genderType: {type: String, required: true},
  },
  methods: {
    capitalizeFirstLetter,
  },
}
</script>

<style lang="scss" scoped>
.wrapper {
  display: flex;
  align-items: center;
  justify-content: center;

  width: fit-content;
  height: 100%;
  gap: 5px;
  padding: 6px 8px;

  border-radius: 2px 12px 12px 2px;

  overflow: hidden;
  &:not(:last-child) {
    margin-right: 6px;
  }
}

.male {
  background: var(--neutral-secondary-color);
}
.female {
  background: #ffe3e8;
}

.undefined {
  background: var(--background-additional-color);
}
</style>
