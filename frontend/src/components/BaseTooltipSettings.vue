<template>
  <div class="settings-container" ref="settings-wrapper">
    <div v-if="isOpenSettings" class="options-container">
      <slot></slot>
    </div>
    <PointsIcon
      :class="['points-icon', isOpenSettings && 'active-points']"
      @click.stop="openSettings"
    />
  </div>
</template>

<script>
import PointsIcon from '@/components/icons/PointsIcon'

export default {
  name: 'BaseTooltipSettings',
  components: {
    PointsIcon,
  },
  props: {
    id: {
      type: [Number, String],
      default: '',
    },
  },
  data() {
    return {
      isOpenSettings: false,
    }
  },
  created() {
    document.addEventListener('click', this.close)
  },
  methods: {
    openSettings() {
      this.isOpenSettings = !this.isOpenSettings
    },
    close() {
      const elements = document.querySelectorAll('.settings-container')

      if (!Array.from(elements).find((el) => el.contains(event.target))) {
        this.isOpenSettings = false
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.settings-container {
  position: relative;

  width: 30px;
  height: 30px;
}

.options-container {
  position: absolute;
  right: -5px;
  bottom: calc(100% + 8px);

  display: flex;
  flex-direction: column;

  white-space: nowrap;

  border-radius: 4px;
  padding: 8px;
  box-shadow: 1px 2px 6px rgba(135, 135, 135, 0.25);

  background: var(--background-secondary-color);

  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 110%;
  color: var(--typography-title-color);
}

.close-options {
  display: none;
}

.points-icon {
  z-index: 3;

  flex-shrink: 0;

  width: 30px;
  height: 30px;

  transition: all 0.3s;
  pointer-events: stroke;

  color: var(--typography-secondary-color);
}

.points-icon:hover {
  border-radius: 100%;

  color: var(--typography-primary-color);
  background-color: var(--button-primary-color);
}

.active-points {
  border-radius: 100%;

  color: var(--typography-primary-color);
  background-color: var(--button-primary-color);
}
</style>
